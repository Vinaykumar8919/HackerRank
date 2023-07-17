import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = 4;
        int row = 2 * n - 1;
        int col = 2 * n - 1;

        int[][] arr = new int[row][col];
        int left = 0, top = 0, right = col - 1, bottom = row - 1;

        while (left <= right && top <= bottom) {
            for (int i = left; i <= right; i++) {
                arr[top][i] = n;
            }
            top++;
            for (int i = top; i <= bottom; i++) {
                arr[i][right] = n;
            }
            right--;
            if (left > right || top > bottom)
                break;
            for (int i = right; i >= left; i--) {
                arr[bottom][i] = n;
            }
            bottom--;
            for (int i = bottom; i >= top; i--) {
                arr[i][left] = n;
            }
            left++;
            n--;
        }

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}



// n=4
/*4 4 4 4 4 4 4 
  4 3 3 3 3 3 4 
  4 3 2 2 2 3 4 
  4 3 2 1 2 3 4 
  4 3 2 2 2 3 4 
  4 3 3 3 3 3 4 
  4 4 4 4 4 4 4 */


//n=5
// 5 5 5 5 5 5 5 5 5 
// 5 4 4 4 4 4 4 4 5 
// 5 4 3 3 3 3 3 4 5 
// 5 4 3 2 2 2 3 4 5 
// 5 4 3 2 1 2 3 4 5 
// 5 4 3 2 2 2 3 4 5 
// 5 4 3 3 3 3 3 4 5 
// 5 4 4 4 4 4 4 4 5 
// 5 5 5 5 5 5 5 5 5 
