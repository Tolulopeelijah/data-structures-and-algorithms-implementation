#include <stdio.h>
void towerofhanoi(int n, char source, char auxilliary, char target){
    if (n==1){
        printf("move %dth from %c to %c\n", n, source, target);
        return;
        
    }
    towerofhanoi(n-1, source, target, auxilliary); //move n-1 to auxiliary
    printf("move %dth from %c to %c\n", n, source, target); //move nth to target
    towerofhanoi(n-1, auxilliary, source, target); //move n-1 to target
}
    
    
    int main()
{
    char source, auxilliary, target;
    int n;
    printf("what will you like to denote source with: \n");
    scanf(" %c", &source);
    printf("what will you like to denote auxilliary with: \n");
    scanf(" %c", &auxilliary);
    printf("what will you like to denote target with: \n");
    scanf(" %c", &target);
    printf("how many disks are in the source?: ");
    scanf(" %d", &n);
    towerofhanoi(n, source, auxilliary, target);

    return 0;
}
