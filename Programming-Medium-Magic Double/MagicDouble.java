import java.util.InputMismatchException;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;
public class MagicDouble {
	public static void main(String[] args) throws IOException, InterruptedException {
		try {
			Scanner kb = new Scanner(System.in);
			System.out.print("Enter a: ");
			double a = kb.nextDouble();
			System.out.print("Enter b: ");
			double b = kb.nextDouble();
			System.out.print("Enter c: ");
			double c = kb.nextDouble();
			if (a < b && a < c && c < b) {
				System.out.println("You Pass Mission #1");
				if ((a + b + "").equals(c / c + "")) {
					System.out.println("You Pass Mission #2");
					if (a + b != a + b) {
						System.out.println("You Pass Mission #3");
						if (c / c != c / c) {
							System.out.println("You Pass Mission #4");
							String flag = a + "_" + b + "_" + c + "_" + (a + b) + "_" + (c / c);
							flag = flag.toUpperCase();
							flag = getMd5(flag);
							System.out.println("WCTF23{" + flag + "}");
						}
					}
				}
			}
		} catch (InputMismatchException a) {
			System.out.println("Input Mismatch");
		}
	}
	
	private static String getMd5(String s) {
		try {
			MessageDigest md = MessageDigest.getInstance("MD5");
			byte[] array = md.digest(s.getBytes());
			StringBuffer sb = new StringBuffer();
			for (int i = 0; i < array.length; i++) {
				sb.append(Integer.toHexString((array[i] & 0xFF) | 0x100).substring(1, 3));
			}
			return sb.toString();
		} catch (NoSuchAlgorithmException e) {
			return "";
		}
	}
}
