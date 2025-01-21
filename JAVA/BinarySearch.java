public class BinarySearch {
    public static void main(String[] args) {
        System.out.println(search(new double[]{1,2,3,4,5,6,7,8,9}, 6));
    }

    public static int   search(double[] arrayOfNumbers, double item){
        int firstIndex = 0;
        int lastIndex = arrayOfNumbers.length - 1;
        int itemIndex = 0;
        while(firstIndex <= lastIndex){
            System.out.println("running");
            int middleIndex = (firstIndex + lastIndex)/2;
            double guess = arrayOfNumbers[middleIndex];
            if(guess == item){
                itemIndex = middleIndex;
                return itemIndex;
            }
            if (guess > item){
                lastIndex = middleIndex -1;
            }else{
                firstIndex = middleIndex +1;
            }
        }
        return itemIndex;
    }
}
