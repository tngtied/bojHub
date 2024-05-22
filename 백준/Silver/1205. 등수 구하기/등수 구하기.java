import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

	public static void main(String[] args) throws IOException {
		int n, point, p;
		StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
		n = Integer.parseInt(stringTokenizer.nextToken());
		point = Integer.parseInt(stringTokenizer.nextToken());
		p = Integer.parseInt(stringTokenizer.nextToken());
		boolean foundFlag = false;
		if (n != 0) {
			stringTokenizer = new StringTokenizer(bufferedReader.readLine());
		}
		int currentPoint = 0;
		int position = n + 1;
		for (int i = 0; i < n; i++) {
			currentPoint = Integer.parseInt(stringTokenizer.nextToken());
			if (currentPoint <= point && !foundFlag) {
				foundFlag = true;
				position = i + 1;
			}
		}
		if (currentPoint < point || n + 1 <= p) {
			bufferedWriter.write(String.valueOf(position));
		} else {
			bufferedWriter.write("-1");
		}

		bufferedWriter.flush();
		bufferedWriter.close();
	}

}