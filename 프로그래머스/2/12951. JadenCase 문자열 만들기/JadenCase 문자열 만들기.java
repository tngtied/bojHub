import java.util.StringTokenizer;

class Solution {

	String jadenCase(String given) {
		char[] givenCharList = given.toCharArray();
		for (int i = 0; i < givenCharList.length; i++) {
			if (i == 0) {
				givenCharList[i] = Character.toUpperCase(givenCharList[i]);
			} else {
				givenCharList[i] = Character.toLowerCase(givenCharList[i]);
			}
		}
		return String.valueOf(givenCharList);
	}

	public String solution(String s) {
		StringTokenizer stringTokenizer = new StringTokenizer(s);
		String word;
		char[] sCharArray = s.toCharArray();
		String result = "";
		int loadedLength = 0;
		if (sCharArray[loadedLength] == ' ') {
			while (sCharArray[loadedLength] == ' ') {
				loadedLength += 1;
				result += " ";
			}
		}
		while (stringTokenizer.countTokens() != 0) {
			word = stringTokenizer.nextToken();
			result += jadenCase(word);
			loadedLength += word.length();
			if (stringTokenizer.countTokens() != 0) {
				while (sCharArray[loadedLength] == ' ') {
					loadedLength += 1;
					result += " ";
				}
			}
			System.out.println(String.format("word %s loaded length %d", word, loadedLength));
		}
		if (loadedLength < sCharArray.length && sCharArray[loadedLength] == ' ') {
			while (loadedLength < sCharArray.length && sCharArray[loadedLength] == ' ') {
				loadedLength += 1;
				result += " ";
			}
		}
		return result;

	}
}