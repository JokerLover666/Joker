/*
 * bubble_sort.c
 *
 * 冒泡排序（Bubble Sort）的 C 语言实现。
 *
 * 原理：
 *   依次比较相邻的两个元素，如果前一个比后一个大（升序）就交换它们。
 *   每一趟遍历都会把当前未排序部分中最大的元素"冒泡"到末尾。
 *
 * 复杂度：
 *   最好 O(n)       —— 数组本身有序，一趟扫描即可提前结束
 *   平均 O(n^2)
 *   最坏 O(n^2)
 *   空间 O(1)       —— 原地排序，稳定排序
 */

#include <stdio.h>
#include <stddef.h>   /* size_t */

/* 交换两个整数的值 */
static void swap_int(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

/*
 * 冒泡排序（升序）。
 *
 * arr  : 待排序数组
 * n    : 元素个数
 *
 * 外层循环控制排序趟数，共 n - 1 趟；
 * 内层循环进行比较与交换，每趟结束后末尾的有序区间增加 1 个元素。
 * 使用 swapped 标记做优化：如果某一趟没有发生任何交换，
 * 说明数组已经有序，可以提前退出。
 */
void bubble_sort(int arr[], size_t n)
{
    if (arr == NULL || n < 2)
        return;

    for (size_t i = 0; i + 1 < n; i++) {
        int swapped = 0;

        /* 未排序区间为 [0, n - i - 1]，最后一个位置是 n - i - 1 */
        for (size_t j = 0; j + 1 < n - i; j++) {
            if (arr[j] > arr[j + 1]) {
                swap_int(&arr[j], &arr[j + 1]);
                swapped = 1;
            }
        }

        /* 本趟没有发生交换，说明已经有序 */
        if (!swapped)
            break;
    }
}

/* 打印数组，元素之间用空格分隔 */
void print_array(const int arr[], size_t n)
{
    printf("[");
    for (size_t i = 0; i < n; i++) {
        printf("%d", arr[i]);
        if (i + 1 < n)
            printf(", ");
    }
    printf("]\n");
}

int main(void)
{
    int arr[] = {64, 34, 25, 12, 22, 11, 90, 5, 77, 1};
    size_t n = sizeof(arr) / sizeof(arr[0]);

    printf("排序前: ");
    print_array(arr, n);

    bubble_sort(arr, n);

    printf("排序后: ");
    print_array(arr, n);

    return 0;
}
