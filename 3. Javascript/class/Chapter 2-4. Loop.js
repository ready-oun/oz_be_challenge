let sum = 0;

while (i = 1; i <= 50; i +=1){
    if (i % 2 !== 0) {
        sum += i;
        console.log(i, sum);
    }
}
console.log(sum)