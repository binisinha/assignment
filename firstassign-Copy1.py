{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2030,2065,2100,2135,2170,2205,2240,2275,2310,2345,2380,2415,2450,2485,2520,2555,2590,2625,2660,2695,2730,2765,2800,2835,2870,2905,2940,2975\n"
     ]
    }
   ],
   "source": [
    "nl=[]\n",
    "for x in range(2000, 3000):\n",
    "    if (x%7==0) and (x%5!=0):\n",
    "        nl.append(str(x))\n",
    "print (','.join(nl))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your first Namemndsa\n",
      "Enter your last Nameasdk\n"
     ]
    }
   ],
   "source": [
    "firstnm=input(\"Enter your first Name\")\n",
    "lastnm=input(\"Enter your last Name\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "14698592.829487206\n"
     ]
    }
   ],
   "source": [
    "vol=[]\n",
    "r=12\n",
    "vol=4/3*(3.14**r*r)\n",
    "print(vol)"
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
