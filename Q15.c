/*Q-15 Solving ODE y ' = y − t ^2 + 1 using Euler method */


#include<stdio.h>
#include<math.h>

float func(float y, float t)
{
  return (y-t*t+1); 
}

int main()
{
  float ysol[10],yerror[10];  //ysol for Euler solution, yerror for error erroring in each step
  ysol[0]=0.5;
  yerror[0]=((0)*1.0/5+1.0)*((0)*1.0/5+1.0)-0.5*exp((0)*1.0/5)-ysol[0];
  for(int i=0;i<9;i++)
    {
      ysol[i+1]=ysol[i]+0.2*func(ysol[i],i*1.0/5.0);
      yerror[i+1]=((i+1)*1.0/5+1.0)*((i+1)*1.0/5+1.0)-0.5*exp((i+1)*1.0/5)-ysol[i+1];
      printf("Value of y at t=%f is %f\n",i*1.0/5,ysol[i]);
    }
  printf("Value of y at t=%f is %f\n",2.0,ysol[2]);
  for(int i=0;i<=9;i++)
    {
      printf("Error at %d th step is=%f\n",i+1,yerror[i]);
    }
  return 0;
}
