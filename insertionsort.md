## Başlangıç durumu: [22,27,16,2,18,6]

###### Sorting aşamaları:

1. [2,27,16,22,18,6]
2. [2,6,16,22,18,27]
3. [2,6,16,22,18,27]
4. [2,6,16,18,22,27]
5. [2,6,16,18,22,27]

###### Big-O gösterimi:

Listedeki eleman sayımıza n dersek
1. adım için yapılan sorgu sayısı = n
2. adım için yapılan sorgu sayısı = n-1
3. adım için yapılan sorgu sayısı = n-2
4. adım için yapılan sorgu sayısı = n-3
5. adım için yapılan sorgu sayısı = n-4

Yapılan toplam sorgu sayısı = n*(n+1) / 2 = O(n^2)

###### Time complexity:

Average Case = [27,16,2,18]

Best Case = [22]

Worst Case = [6]

###### 18 Average case kapsamına girer.

###### [7,3,5,8,2,9,4,15,6] dizisi:

1. [2,3,5,8,7,9,4,15,6]
2. [2,3,5,8,7,9,4,15,6]
3. [2,3,4,8,7,9,5,15,6]
4. [2,3,4,6,7,9,5,15,8]



