package com.example;

public class App 
{
    public static void main( String[] args )
    {
        Math m = new Math();
        int r1 = m.add(9,3);
        int r2 = m.substract(9,3);
        int r3 = m.multiply(9,3);
        double r4 = m.divide(9,3);

        System.out.println(r1);
        System.out.println(r2);
        System.out.println(r3);
        System.out.println(r4);
    }
}
