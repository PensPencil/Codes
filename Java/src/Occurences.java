import java.util.Scanner;
public class Occurences{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = in.nextInt();
        System.out.print("Enter a number to be searched: ");
        int m = in.nextInt();
        int count = 0;
        while(n>0){
            int rem = n%10;
            if(rem == m){
                count++;
            }
            n = n/10;
        }
        System.out.println(m + " occurs "+ count+" time(s) in "+n);

    }
}