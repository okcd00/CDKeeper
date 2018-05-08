import java.math.*;
import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner in=new Scanner(System.in);
        while(in.hasNext()){
            BigDecimal val=in.nextBigDecimal();
            int n=in.nextInt();
            BigDecimal ret=val.pow(n).stripTrailingZeros();
            System.out.println( ret.toPlainString().replaceAll("^0", "") );
        }
    }
}