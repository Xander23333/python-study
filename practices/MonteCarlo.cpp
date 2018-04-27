#include<iostream>
#include<ctime>
#include<cstdlib>
using namespace std;

int main(){
  srand((unsigned int)time(NULL));
  time_t t1;
  time(&t1);
  long long N=1e5;
  long long fits=0;
  double d,a,b;
  for (long long k=0;k<=N*N;++k){
    a=rand()/RAND_MAX;
    b=rand()/RAND_MAX;
    d=a*a+b*b;
    if (d<=1.0) ++fits;
  }
  double pi=(double)fits/(N*N)*4;
  time_t t2;
  time(&t2);
  printf("已运行%d秒\n",t2-t1);
  printf("pi by Monte Carlo Method with C++ is %.16f\n",pi);
}