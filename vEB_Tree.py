# van Emde Boas Tree implementation on insert, delete and successor

# Maintain min and max of every structure
Successor(V, x):
	i = high(x)
	if low(x) < V.cluster[i].max:
		j = Successor(V.cluster[i].low(x))
	else:
		i = Success(V.summary, high(x))
		j = V.cluster[i].min
	return index(i, j)

# T(n) = O(log(log(u)))

# Don't store min recursively
Insert(V, x):
	if V.min is None:
		V.min = V.max = x
		return
	if x < V.min:
		x, V.min = V.min, x
	if x > V.max:
		V.max = x
	if V.cluster[high(x)].min is None:
		Insert(V.summary, high(x))
	insert(V.cluster[high(x)], low(x))

# T(u) = O(log(log(u)))

Delete(V, x):
	if x == V.min:
		i = V.summary.min
		if i is None:
			V.min = V.max = None
		 	return
		 x = V.min = index(i, V.cluster[i].min)
	Delete(V.cluster[high(x)], low(x))
	if V.cluster[high(x)].min is None:
		Delete(V.summary, high(x))
	if x == V.max:
		if V.summary.max = None:
			V.max = V.min
		else:
			i = V.summary.max
			v.max = index(i, V.cluster[i].max)

# T(u) = O(log(log(u)))
