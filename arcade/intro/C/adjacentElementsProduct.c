int adjacentElementsProduct(arr_integer i) {
	int t = i.arr[0]*i.arr[1], m = 0;
	while (--i.size) {
		if (t < i.arr[m]*i.arr[m+1]) t = i.arr[m]*i.arr[m+1];
		m++;
	}
	return t;
}
