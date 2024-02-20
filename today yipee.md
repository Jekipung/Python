```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#pragma warning(disable:4996)

// 값을 받을 문자열 함수 str
char str[20];

// 노드의 탑을 볼 struct stack
typedef struct stack {
    struct node* top;
}Stack;

// 문자값과 다음 문자를 볼 next가 담긴 struct node
typedef struct node {
    char data;
    struct node* next;
}Node;

// top값의 초기화하는 함수
void init(Stack* ps) {
    ps->top = NULL;
}

// 스택이 비어있는지 확인하는 함수
int isEmpty(Stack* ps) {
    if (ps->top == NULL) {
        return 1;
    }
    else
        return 0;
}

// 값을 하나씩 받는 함수
void push(Stack* ps, char d) {
    Node* newNode = malloc(sizeof(Node));
    newNode->data = d;
    newNode->next = ps->top;
    ps->top = newNode;
}

// 값을 하나씩 빼는 함수
char pop(Stack* ps) {
    char rdata;
    Node* rnode;

    if (isEmpty(ps)) {
        printf("stack memory error");
        exit(-1);
    }

    rdata = ps->top->data;
    rnode = ps->top;

    ps->top = ps->top->next;
    free(rnode);

    return rdata;
}


// 메인 함수
int main() {
    printf("문자열을 입력하시오: ");
    scanf("%[^\n]s", str);
    Stack S1;
    for (int i = 0; i < strlen(str); i++) {
        push(&S1, str[i]);
    }

    int i;
    for (i = 0; i < strlen(str); i++) {
        str[i] = pop(&S1);
    }
    str[i] = '\0';

    printf("%s", str);

    return 0;
}
```
