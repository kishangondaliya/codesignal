bool almostIncreasingSequence(arr_integer sequence) {
	int arrayLength=sequence.size;
	int i = 0;
	int count = 0;
	int flag = false;
	int max = -100000;
	int secondMax = -100000;

	for (i = 0; i < arrayLength; i++) {
		if (sequence.arr[i] > max) {
			secondMax = max;
			max = sequence.arr[i];
		} else if (sequence.arr[i] > secondMax) {
			if (flag) {
				max = sequence.arr[i];
				flag = false;
			} else {
				secondMax = sequence.arr[i];
				flag = true;
				count++;
			}
		} else {
			count++;
		}
	}


	if (count == 1) {
		return true;
	} else {
		return false;
	}

}
