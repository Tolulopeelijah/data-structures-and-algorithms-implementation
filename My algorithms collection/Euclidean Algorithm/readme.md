# Euclidean Algorithm

## Introduction

The Euclidean algorithm is an efficient method for computing the greatest common divisor (GCD) of two numbers. It is based on the principle that the GCD of two numbers also divides their difference.

## Problem Statement

Given two integers, a and b, find their greatest common divisor.

## Algorithm

The algorithm repeatedly replaces the larger number by its remainder when divided by the smaller number until one of the numbers becomes zero. The other number then becomes the GCD.

### Pseudocode

```plaintext
procedure EuclideanAlgorithm(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a