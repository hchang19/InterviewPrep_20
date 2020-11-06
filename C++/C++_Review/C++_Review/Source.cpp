#include <iostream>
#include <string>
using namespace std;

class sampleParent {
public:
	sampleParent(string hair_color = "grey", int age = 0, int wisdom = 0) {
		cout << "I am being called from the constructor" << endl;
		m_age = age;
		m_wisdom = wisdom;
		m_hair_color = hair_color;
	}

	virtual ~sampleParent() {
		cout << "I am being deleted" << endl;
	}

	string getHairColo() {
		return m_hair_color;
	}

	int getAge() {
		return m_age;
	}

	int getWisdom() {
		return m_wisdom;
	}

private:
	int m_age;
	int m_wisdom;
	string m_hair_color;
};


int main() {
	cout << "hello I am back in C++" << endl;

	sampleParent a;
	cout << a.getAge() << endl;
}

