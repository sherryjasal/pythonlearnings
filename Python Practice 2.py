{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Use for, .split(), and if to create a Statement that will print out words that start with 's':    \n",
    "st = 'Print only the words that start with s in this sentence'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "start\n",
      "s\n",
      "sentence\n"
     ]
    }
   ],
   "source": [
    "for start_letter in st.split():\n",
    "    if start_letter[0] == 's':\n",
    "        print(start_letter)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "2\n",
      "4\n",
      "6\n",
      "8\n"
     ]
    }
   ],
   "source": [
    "#Use range() to print all the even numbers from 0 to 10:\n",
    "\n",
    "for num in range(0,10):\n",
    "    if num % 2 == 0:\n",
    "        print ('{}'.format(num))\n",
    "    else:\n",
    "        pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "lst = [num for num in range(0,10) if num % 2 == 0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 2, 4, 6, 8]"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lst"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.\n",
    "\n",
    "my_list = [num for num in range(1,50) if num % 3 == 0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Go through the string below and if the length of a word is even print \"even!\"\n",
    "st = 'Print every word in this sentence that has an even number of letters'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "word\n",
      "in\n",
      "this\n",
      "sentence\n",
      "that\n",
      "an\n",
      "even\n",
      "number\n",
      "of\n"
     ]
    }
   ],
   "source": [
    "st =  st.split()\n",
    "\n",
    "for word in st: \n",
    "    if len(word) % 2 == 0:\n",
    "        print(word)     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Write a program that prints the integers from 1 to 100. But for multiples of three print \"Fizz\" instead of the number, and for the multiples of five print \"Buzz\". For numbers which are multiples of both three and five print \"FizzBuzz\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "Fizz\n",
      "4\n",
      "Buzz\n",
      "Fizz\n",
      "7\n",
      "8\n",
      "Fizz\n",
      "Buzz\n",
      "11\n",
      "Fizz\n",
      "13\n",
      "14\n",
      "FizzBuzz\n",
      "16\n",
      "17\n",
      "Fizz\n",
      "19\n",
      "Buzz\n",
      "Fizz\n",
      "22\n",
      "23\n",
      "Fizz\n",
      "Buzz\n",
      "26\n",
      "Fizz\n",
      "28\n",
      "29\n",
      "FizzBuzz\n",
      "31\n",
      "32\n",
      "Fizz\n",
      "34\n",
      "Buzz\n",
      "Fizz\n",
      "37\n",
      "38\n",
      "Fizz\n",
      "Buzz\n",
      "41\n",
      "Fizz\n",
      "43\n",
      "44\n",
      "FizzBuzz\n",
      "46\n",
      "47\n",
      "Fizz\n",
      "49\n",
      "Buzz\n",
      "Fizz\n",
      "52\n",
      "53\n",
      "Fizz\n",
      "Buzz\n",
      "56\n",
      "Fizz\n",
      "58\n",
      "59\n",
      "FizzBuzz\n",
      "61\n",
      "62\n",
      "Fizz\n",
      "64\n",
      "Buzz\n",
      "Fizz\n",
      "67\n",
      "68\n",
      "Fizz\n",
      "Buzz\n",
      "71\n",
      "Fizz\n",
      "73\n",
      "74\n",
      "FizzBuzz\n",
      "76\n",
      "77\n",
      "Fizz\n",
      "79\n",
      "Buzz\n",
      "Fizz\n",
      "82\n",
      "83\n",
      "Fizz\n",
      "Buzz\n",
      "86\n",
      "Fizz\n",
      "88\n",
      "89\n",
      "FizzBuzz\n",
      "91\n",
      "92\n",
      "Fizz\n",
      "94\n",
      "Buzz\n",
      "Fizz\n",
      "97\n",
      "98\n",
      "Fizz\n",
      "Buzz\n"
     ]
    }
   ],
   "source": [
    "for num in range(1,101):\n",
    "    if num % 3 == 0 and num % 5 == 0:\n",
    "        print (\"FizzBuzz\")\n",
    "    elif num % 3 == 0:\n",
    "        print(\"Fizz\")\n",
    "    elif num % 5 == 0:\n",
    "        print(\"Buzz\")\n",
    "    else:\n",
    "        print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Use List Comprehension to create a list of the first letters of every word in the string below:\n",
    "st = 'Create a list of the first letters of every word in this string'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "lst = [word[0] for word in st.split()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['C', 'a', 'l', 'o', 't', 'f', 'l', 'o', 'e', 'w', 'i', 't', 's']"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lst"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
