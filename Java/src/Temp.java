import java.sql.SQLOutput;
import java.util.Scanner;

public class Temp{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter a temperature in C :");
        float C = in.nextFloat();
        double far = (float) (1.8 * C + 32);
        System.out.println(C + " degree celcius is " + far + " fahreheit");
    }
}
