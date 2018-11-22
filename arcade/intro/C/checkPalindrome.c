bool checkPalindrome(char * inputString) {
	int len = strlen(inputString);
	for (int i = 0; i < len/2; i++) if (inputString[i] != inputString[len-i -1]) return false;
	return true;
}
