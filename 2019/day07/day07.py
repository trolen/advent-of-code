#! /usr/bin/env python3

import itertools
import queue
import threading
import time


def read_data(filename):
    with open(filename, 'rt') as file:
        return file.readline().strip()


class intCode (threading.Thread):
    def __init__(self, raw_data):
        threading.Thread.__init__(self)
        self._data = [int(x) for x in raw_data.split(',')]
        self._in_queue = queue.Queue(10)
        self._out_queue = queue.Queue(10)
        self._queue_lock = threading.Lock()
        self._is_finished = False

    def input(self, val):
        self._queue_lock.acquire(blocking=True)
        self._in_queue.put(val)
        self._queue_lock.release()

    def output(self):
        self._queue_lock.acquire(blocking=True)
        result = None if self._out_queue.empty() else self._out_queue.get()
        self._queue_lock.release()
        return result

    def finished(self):
        return self._is_finished

    def _calc_parameter_modes(self, data):
        opcode = data % 100
        pModeA = (data // 100) % 10
        pModeB = (data // 1000) % 10
        pModeC = (data // 10000) % 10
        return (opcode, pModeA, pModeB, pModeC)

    def _get_data_value(self, pos, mode):
        parm = self._data[pos]
        return self._data[parm] if mode == 0 else parm

    def _is_queue_empty(self):
        self._queue_lock.acquire(blocking=True)
        result = self._in_queue.empty()
        self._queue_lock.release()
        return result

    def _get_input(self):
        while self._is_queue_empty():
            time.sleep(1)
        self._queue_lock.acquire(blocking=True)
        result = self._in_queue.get()
        self._queue_lock.release()
        return result

    def _put_output(self, value):
        self._queue_lock.acquire(blocking=True)
        self._out_queue.put(value)
        self._queue_lock.release()

    def run(self):
        pos = 0
        while True:
            (opcode, pModeA, pModeB, pModeC) = self._calc_parameter_modes(self._data[pos])
            if opcode == 99:
                self._is_finished = True
                return
            incr = 0
            if opcode in (1, 2):
                valA = self._get_data_value(pos + 1, pModeA)
                valB = self._get_data_value(pos + 2, pModeB)
                parmC = self._data[pos + 3]
                self._data[parmC] = valA + valB if opcode == 1 else valA * valB
                incr = 4
            elif opcode == 3:
                parmA = self._data[pos + 1]
                self._data[parmA] = self._get_input()
                incr = 2
            elif opcode == 4:
                valA = self._get_data_value(pos + 1, pModeA)
                self._put_output(valA)
                incr = 2
            elif opcode in (5, 6):
                valA = self._get_data_value(pos + 1, pModeA)
                valB = self._get_data_value(pos + 2, pModeB)
                if (opcode == 5 and not valA == 0) or (opcode == 6 and valA == 0):
                    pos = valB
                else:
                    incr = 3
            elif opcode in (7, 8):
                valA = self._get_data_value(pos + 1, pModeA)
                valB = self._get_data_value(pos + 2, pModeB)
                parmC = self._data[pos + 3]
                if (opcode == 7 and valA < valB) or (opcode == 8 and valA == valB):
                    self._data[parmC] = 1
                else:
                    self._data[parmC] = 0
                incr = 4
            pos += incr


def get_thread_output(thread):
    while True:
        result = thread.output()
        if result is not None:
            return result
        time.sleep(1)


def calc_thruster_signal(raw_data, phase_settings, feedback_mode=False):
    threads = []
    signal = 0
    for n in range(0, 5):
        thread = intCode(raw_data)
        thread.input(phase_settings[n])
        thread.input(signal)
        thread.start()
        threads.append(thread)
        signal = get_thread_output(thread)
    while feedback_mode:
        n_alive = 0
        for n in range(0, 5):
            thread = threads[n]
            if thread.finished():
                break
            n_alive += 1
            thread.input(signal)
            signal = get_thread_output(thread)
        if n_alive < 5:
            break
    for thread in threads:
        thread.join()
    return signal


def find_max_thruster_signal(raw_data, feedback_mode=False):
    sequence = [0, 1, 2, 3, 4]
    if feedback_mode:
        sequence = [5, 6, 7, 8, 9]
    perms = itertools.permutations(sequence)
    signals = []
    for p in perms:
        signals.append(calc_thruster_signal(raw_data, p, feedback_mode))
    return max(signals)


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    result = find_max_thruster_signal(raw_data)
    print('Max Thruster Signal: {0}'.format(result))
    result = find_max_thruster_signal(raw_data, feedback_mode=True)
    print('Max Signal (feedback mode): {0}'.format(result))
