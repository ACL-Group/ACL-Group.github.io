#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <time.h>
#include <math.h>

using namespace std;

const int DISTRIBUTION = 1;
const int MINE = 2;

char allFile[100], senFile[100];
bool ifSensitive[10000];
vector<vector<int> > rows;
vector<vector<int> > buffer;
vector<int> sensitive;
int MAXNUM = -1;
int bmax = 100000;
int policy = MINE;
int sup[100000000];
double rho = 0.7;

bool* all;

struct Trie_node {
	int data, num;
	vector<Trie_node*> branch;
	Trie_node() {
		data = -1;
		num = 0;
	}
	Trie_node(int a) {
		data = a;
		num = 1;
	}
};

class Trie {
public:
	Trie_node* root;
	Trie() {
		root = NULL;
	}
	//default: getSupport(&rec, 0, root)
	int getSupport(vector<int> *record) {
		return getSupport(record, 0, root);
	}
	int getSupport(vector<int> *record, int pos, Trie_node* location) {
		if (pos == (*record).size())
			return location->num;
		int position = 0, i;
		int count = 0;
		bool flag;
		for (i=0; i<location->branch.size(); ++i)
			if (location->branch[i]->data == (*record)[pos])
				count += getSupport(record, pos+1, location->branch[i]);
			else if (location->branch[i]->data < (*record)[pos])
				count += getSupport(record, pos, location->branch[i]);
		return count;
	}
	int insert(vector<int> *record) {
		int result = 1, position = 0, i, j=0;
		if (root == NULL) root = new Trie_node;
		bool flag;
		Trie_node *location = root;
		while (location != NULL && j<(*record).size()) {
			flag = false;
			for (i=0; i<location->branch.size(); ++i)
				if (location->branch[i]->data == (*record)[j]) {
					flag = true;
					break;
				}
			if (!flag) {
				location->branch.push_back(new Trie_node((*record)[j]));
				//cout << "new "<<(*record)[j]<<' '<<location->branch.back()->num<<endl;
				location = location->branch.back();
			} else {
				location = location->branch[i];
				++location->num;
			}
			++position;
			++j;
		}
		cout<<position<<endl;
	}
	~Trie() {}
};

Trie supportTree;

void readFile(char* fileName) {
	ifstream file(fileName);
	string line;
	int num;
	while (!getline(file, line, '\n').eof()) {
		rows.push_back(vector<int> ());
		vector<int>& row = rows.back();
		istringstream reader(line);
		while (!reader.eof() && reader >> num) {
			if (num > MAXNUM) MAXNUM = num;
			row.push_back(num);
		}
		supportTree.insert(&row);
		cout<<endl;
	}
	file.close();
	
	vector<int> test;
	test.push_back(2);
	cout << "|  "<<supportTree.getSupport(&test)<<endl;
}

void readSenFile(char* fileName) {
	ifstream file(fileName);
	string line;
	int num;
	for (int i=1; i<=MAXNUM; ++i)
		ifSensitive[i] = false;
	while (!getline(file, line, '\n').eof()) {
		istringstream reader(line);
		reader >> num;
		ifSensitive[num] = true;
		sensitive.push_back(num);
	}
}

void shuffle(vector<vector<int> > *record) {
	random_shuffle((*record).begin(), (*record).end());
}

void generateQids(int i, int n, string s) {
	if (n==rows[i].size()) {
		istringstream istr(s);
		buffer.push_back(vector<int> ());
		vector<int>& qid = buffer.back();
		int tmp;
		while (istr>>tmp) qid.push_back(tmp);
		return;
	}
	stringstream sAdd;
	sAdd << s << ' ' << rows[i][n];
	generateQids(i, n+1, s);
	generateQids(i, n+1, sAdd.str());
}

void updateSup() {
	for (int i=0; i<buffer.size(); ++i) {
		if (buffer[i].size() == 0){
			sup[i] = -1;
			continue;
		}
		sup[i] = supportTree.getSupport(&buffer[i]);
		
		for (int j=0;j<buffer[i].size();++j)cout<<buffer[i][j]<<' ';cout<<":  ";
		cout<<sup[i]<<endl;
	}
}

void checkBuffer() {
	for (int i=0; i<buffer.size(); ++i) {
		
	}
}

void partialSuppressor() {
	bool safe = true;
	int bufferSize = 0;
	int i = 0;
	int recordSize = rows.size();
	long int s;
	for (int i=0; i<bufferSize; ++i) sup[i] = 0;
	while (true) {
		while (bufferSize < bmax && i < recordSize) {
			s = pow(2, rows[i].size());
			if (bufferSize + s > bmax) break;
			else {
				generateQids(i, 0, "");
				++i;
			}
		}
		updateSup();
		checkBuffer();
		break;
	}
}

int main(int argc, char* argv[]) {
	strcpy(allFile, argv[1]);
	strcpy(senFile, argv[2]);
	srand((int)time(0));
	readFile(allFile);
	readSenFile(senFile);
	shuffle(&rows);
	partialSuppressor();
	return 0;
}