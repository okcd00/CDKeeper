import java.math.*;
import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner in = new Scanner(new BufferedInputStream(System.in));
        //BigDecimal one = new BigDecimal(1);
        BigDecimal eight = new BigDecimal(8);
        String s;
        while (in.hasNext())
        {
            s = in.nextLine();
            BigDecimal ans = new BigDecimal(0);
            BigDecimal wei = new BigDecimal(1);
            for (int i=2;i<s.length();i++){
                wei = wei.divide(eight);
                //System.out.println(wei.toString());
                ans = ans.add(new BigDecimal(s.charAt(i)-48).multiply(wei));
                //System.out.println(ans);
                //public char charAt(int index)����ָ���������� char ֵ��������ΧΪ�� 0 �� length() - 1�����еĵ�һ�� char ֵλ������ 0 �����ڶ���λ������ 1 �����������ƣ�������������������
                //multiply()Ϊָ���ݡ�
                //��char������ת���ɵ�int������-48����Ϊ���ǵ�ASCII��ֵǡ�����48
            }
            System.out.println(s+" [8] = "+ans.toString()+" [10]");
        }
    }
}