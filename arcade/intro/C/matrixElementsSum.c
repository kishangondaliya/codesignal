int matrixElementsSum(arr_arr_integer m) {
	int r = 0, i = 0, j;

	for (; i < m.arr[0].size; i++) {
		for(j = 0; j < m.size; j++) {
			if (m.arr[j].arr[i])
				r += m.arr[j].arr[i];
			else break;
		}
	}
	return r;
}

