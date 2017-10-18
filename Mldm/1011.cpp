#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
using namespace std;

const int maxlen=1000;
enum error_code{success,underflow,overflow};

class stack{
	public:
		stack();
		bool empty();
		bool full();
		int get_top(char &x);
		int get_top(int &x);
		int push(const char x);
		int push(const int x);
		int pop();
	private:
		int count;
		char data[maxlen];
		int data2[maxlen];	
};

stack::stack(){
	count=0;    
}

bool stack::empty(){
	return 0 == count;
}

bool stack::full(){
	return count == maxlen;
}

int stack::get_top(char &x){
	if(empty()){
		return underflow;
	}
	else{
		x = data[count-1];
		return success;
	}
}

int stack::get_top(int &x){
	if(empty()){
		return underflow;
	}
	else{
		x = data2[count-1];
		return success;
	}
}

int stack::pop(){
	if(empty()){
		return underflow;
	}
	else{
		count--;
		return success;
	}
}

int stack::push(const char x){
	if(full()){
		return overflow;
	}
	else{
		data[count]=x;
		count++;
		return success;
	}
}
int stack::push(const int x){
	if(full()){
		return overflow;
	}
	else{
		data2[count]=x;
		count++;
		return success;
	}
}

bool isoperator(char x){
	switch(x){
		case '+': return true; break;
		case '-': return true; break;
		case '*': return true; break;
		case '/': return true; break;
		case '(': return true; break;
		case ')': return true; break;
		case '#': return true; break;
		default:return false;
	}
}

int priority(char oper1,char oper2) 
{  
    int pri;  
    switch(oper1)  
    {  
        case '+':  
        case '-':  
            if(oper2=='('||oper2=='#') pri=-1;
  			else pri=1;
  			break;
        case '*':  
        case '/':  
            if(oper2=='+'||oper2=='-'||oper2=='('||oper2=='#') pri=-1;
            else pri=1;
            break;
        case '(':
        	pri=-1;
        	break;
        case ')':  
          	if(oper2=='(') pri=0;
          	else pri=1;
  			break;
        case '#':  
            if(oper2!='#') pri=1;
			else pri=-1;
    }  
    
    return pri;  
}  

int calculate(int x,int y,char oper)
{
	//cout<<oper<<endl;
	switch(oper){
		case '+':return x+y;break;
		case '-':return y-x;break;
		case '*':return x*y;break;
		case '/': 	if(x!=0){
						return y/x;
						break;
					}
					else{
						cout<<"can not divide 0";
					}
	}
}


int NumberSplicing(char ch[])
{  
    int temp =0; 
    static int len = 10;  
  
    for(int n=0;n<strlen(ch);n++)  
    {  
        char c = ch[n];  
        c-='0';   
        temp = temp *10 + c;  
    } 
	
	return temp;  
}   

void solve(string text)
{
	stack data_sym; 
	stack data_num; 
	int num1,num2;
	char top_char; 
	char temp_c;
	char temp_num[maxlen];
	int flag=0,i=1,j=0; //warning->i=1
	int num=0;
	data_sym.push('#');
	
	temp_c=text[i++];
	
	while(temp_c!='#'||top_char!='#'){
		
		if(isoperator(temp_c))
		{
			if(flag)
			{ 
				temp_num[j]=0;
				j=0;
				num=NumberSplicing(temp_num);
				data_num.push(num);
				num=0;
				flag=0;
			}
			char oper;
			int t;
			switch(priority(temp_c,top_char)){ 
				case 1:
						
						data_sym.get_top(oper);
						data_sym.pop();
						
				    	data_num.get_top(num1);
				    	data_num.pop();
				    	data_num.get_top(num2);
				    	data_num.pop();
				    	t=calculate(num1,num2,oper);
						data_num.push(t);
						break;
				case 0: 
						data_sym.pop();
						temp_c=text[i++];
						break;
				case -1:
						data_sym.push(temp_c);
						temp_c=text[i++];
			}
		}
		else{ 
			temp_num[j++]=temp_c;
			flag=1;
			temp_c=text[i++];
		}
		data_sym.get_top(top_char);
	}
	data_num.get_top(num);
	cout<<num<<endl;
}


int main()
{
	string text;
	cin>>text;
	text = '#' + text + '#';
	solve(text.c_str());
	return 0;
}

