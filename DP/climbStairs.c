#include <stdio.h>

int climbStairs(int n){
    if (n==1){
        return 1;
    }

    if (n==2){
        return 2;
    }

    int first = 1;
    int second = 2;
    int third;
    for (int i=3; i<=n; i++){
        third = first + second;
        first = second;
        second = third; 
    }
    return third;
}

int main(){
    int n = 10;
    int num_foot;
    
    num_foot = climbStairs(n);
    
    printf("%s%d", "answer:",num_foot);
}