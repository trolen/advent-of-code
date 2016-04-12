#include <cstdlib>
#include <fstream>
#include <iostream>
#include <vector>

#include <boost/algorithm/string.hpp>

using namespace std;
using namespace boost;

class Molecules {
  struct Replacement {
    string left;
    string right;
    Replacement(string &l, string &r) {left = l; right = r;}
  };
  vector<Replacement> replacements;

  void parse_lines(const vector<string> &lines);
  bool find_molecule(const string &molecule, const vector<string> &mocecules);
  vector<string> do_replacement(const string &molecule);

public:
  Molecules(const vector<string> &lines);
  int calibrate(const string &molecule);
  int fabricate(const string &molecule);
};

Molecules::Molecules(const vector<string> &lines) {
  parse_lines(lines);
}

void Molecules::parse_lines(const vector<string> &lines) {
  for (vector<string>::const_iterator i = lines.begin(); i != lines.end(); i++) {
    if (i->size() <= 0)
      continue;
    vector<string> words;
    split(words, *i, is_any_of(" "));
    if (words.size() < 3)
      continue;
    replacements.push_back(Replacement(words[0], words[2]));
  }
}

bool Molecules::find_molecule(const string &molecule, const vector<string> &molecules)
{
  for (vector<string>::const_iterator i = molecules.begin(); i != molecules.end(); i++) {
    if (molecule.compare(*i) == 0)
      return true;
  }
  return false;
}

vector<string> Molecules::do_replacement(const string &molecule)
{
  vector<string> molecules;
  for (vector<Replacement>::iterator i = replacements.begin(); i != replacements.end(); i++) {
    size_t found = molecule.find(i->left);
    while (found != string::npos) {
      string m = molecule;
      m.replace(found, i->left.size(), i->right);
      if (!find_molecule(m, molecules))
        molecules.push_back(m);
      found = molecule.find(i->left, found + i->left.size());
    }
  }
  return molecules;
}

int Molecules::calibrate(const string &molecule)
{
  vector<string> molecules = do_replacement(molecule);
  return molecules.size();
}

int Molecules::fabricate(const string &result)
{
  int count = 1;
  vector<string> molecules = do_replacement("e");
  while (molecules.size() > 0 && !find_molecule(result, molecules)) {
    vector<string> new_molecules;
    for (vector<string>::iterator i = molecules.begin(); i != molecules.end(); i++) {
      vector<string> temp = do_replacement(*i);
      for (vector<string>::iterator j = temp.begin(); j != temp.end(); j++) {
        if (j->size() <= result.size())
          new_molecules.push_back(*j);
      }
    }
    molecules.clear();
    for (vector<string>::iterator i = new_molecules.begin(); i != new_molecules.end(); i++) {
      if (!find_molecule(*i, molecules)) {
        molecules.push_back(*i);
      }
    }
    count++;
    cout << count << " " << molecules.size() << endl;
  }
  return count;
}

vector<string> read_input(int argc, char **argv)
{
  if (argc < 2) {
    cout << "Input file name missing" << endl;
    exit(1);
  }

  ifstream ifs(argv[1]);
  if (!ifs.is_open()) {
    cout << "Error opening input file" << endl;
    exit(1);
  }

  vector<string> lines;
  string s;
  while (!ifs.eof()) {
    getline(ifs, s);
    lines.push_back(s);
  }

  ifs.close();

  return lines; 
}

int main(int argc, char **argv)
{
  vector<string> lines = read_input(argc, argv);
  Molecules molecules(lines);
  int n = molecules.calibrate(lines[lines.size() - 1]);
  cout << "Calibration (part 1): " << n << endl;
  n = molecules.fabricate(lines[lines.size() - 1]);
  cout << "Fabricate (part 2): " << n << endl;
}
