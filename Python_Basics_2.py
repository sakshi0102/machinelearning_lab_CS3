{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "mimetype": "text/x-python",
      "nbconvert_exporter": "python",
      "name": "python",
      "pygments_lexer": "ipython3",
      "version": "3.5.4",
      "file_extension": ".py",
      "codemirror_mode": {
        "version": 3,
        "name": "ipython"
      }
    },
    "colab": {
      "name": "Copy of Python_Basics_2.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "toc_visible": true
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ek4PGqxdG5sk",
        "colab_type": "text"
      },
      "source": [
        "### print() function"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "trusted": true,
        "id": "opEi0UOgG5sp",
        "colab_type": "code",
        "outputId": "904108f3-00e4-48de-dfad-4bcc0da2a102",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "# First Program\n",
        "print(\"acropolis\")"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "acropolis\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3LOt0pHO_GkC",
        "colab_type": "text"
      },
      "source": [
        ""
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uSMWmtXTsqH2",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PtDg6KhQG5sn",
        "colab_type": "text"
      },
      "source": [
        "### Comments"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-PwiE7I2G5sv",
        "colab_type": "text"
      },
      "source": [
        "### Variables"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "trusted": false,
        "id": "4h_N96TEG5sx",
        "colab_type": "code",
        "outputId": "f23f1a0f-1915-4524-9ffb-07433e91a071",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "# In Python there is no need to mention the data type\n",
        "\n",
        "var1 = 20      # An integer assignment\n",
        "var2 = 4.123   # A floating point\n",
        "var3 = \"India\" # A string\n",
        "\n",
        "print(var1,' ',var2,' ',var3)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "20   4.123   India\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9BuTFGIHsl1s",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OJjSBDPUG5s1",
        "colab_type": "text"
      },
      "source": [
        "### Assignment"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "trusted": false,
        "id": "D_J2d-iLG5s3",
        "colab_type": "code",
        "outputId": "9276e32f-16e1-48fd-aa87-519ee8ab8c06",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        }
      },
      "source": [
        "# general syntax\n",
        "#variable-name=value\n",
        "\n",
        "# Assigning same value to multiple variables\n",
        "\n",
        "var1 = var2 = var3 = 1\n",
        "print(var1,' ',var2,' ',var3)\n",
        "\n",
        "# Assigning Different values to variable in a single expression\n",
        "\n",
        "var1, var2, var3 = 1, 2.5, \"raghav\"\n",
        "print(var1,' ',var2,' ',var3)\n",
        "\n",
        "# Note: commas can be used for multi-assignments"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "1   1   1\n",
            "1   2.5   nikhar\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Gaq394ter0DP",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xDs1JHtIG5s8",
        "colab_type": "text"
      },
      "source": [
        "### Taking input"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "trusted": true,
        "id": "56pGA0vmG5s9",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "firstname = input(\"Enter your first name: \")\n",
        "lastname = input(\"Enter your second name: \")\n",
        "semester = input(\"Enter your semester: \")"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "mj-0jPpUr4a8",
        "colab_type": "text"
      },
      "source": [
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "trusted": false,
        "id": "U3RV2XeRG5tD",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# run below code\n",
        "age = input(\"Enter your age: \")\n",
        "age = int(age)+5\n",
        "print(age)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MpWzqas4G5tH",
        "colab_type": "text"
      },
      "source": [
        "### Write a program in Python for data type conversion from: \n",
        "- int to string\n",
        "- int to float\n",
        "- string to int\n",
        "- string to float\n",
        "- float to int\n",
        "- float to string"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "trusted": false,
        "id": "EohYaD0jG5tJ",
        "colab_type": "code",
        "outputId": "775e272b-9127-47e0-a3c0-34e84312626f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 119
        }
      },
      "source": [
        "a=10\n",
        "print(str(a))\n",
        "print(float(a))\n",
        "\n",
        "b='20'\n",
        "print(int(b))\n",
        "print(float(b))\n",
        "\n",
        "c=23.56\n",
        "print(int(c))\n",
        "print(str(c))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "10\n",
            "10.0\n",
            "20\n",
            "20.0\n",
            "23\n",
            "23.56\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3SQpXHpgG5tN",
        "colab_type": "text"
      },
      "source": [
        "### Task1: \n",
        "#### WAP to display your infomation like (full name, branch, university name, age, 12th %, hobbies). Store each value into some meaningful variable.  the ouptput of the program should look like"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MhXiJm_ajJJr",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "trusted": false,
        "id": "NcmrqUkXG5tQ",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "\n",
        "full_name=input(\"Enter your full name: \")\n",
        "branch=input(\"Enter your branch: \")\n",
        "university=input(\"Enter your university: \")\n",
        "age=input(\"Enter your age: \")\n",
        "twelth_per=input(\"Enter your 12%: \")\n",
        "hobbies=input(\"Enter your hobbies: \")\n",
        "print(full_name)\n",
        "print(branch)\n",
        "print(university)\n",
        "print(age)\n",
        "print(twelth_per)\n",
        "print(hobbies)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "aUn64sgNG5tU",
        "colab_type": "text"
      },
      "source": [
        "### Commmonly used functions \n",
        "- round(n)\n",
        "- format(n, '0.2f')\n",
        "- format(n,',') # put a comma on thousand place\n",
        "- format(n,'b') # print binary of the number, 'o', 'x'\n",
        "\n",
        "- eval(expression)\n",
        "- chr(n)\n",
        "- ord(character)\n",
        "- bin(n), oct(n), hex(n)\n",
        "\n",
        "- #### function on string/character data\n",
        "- isdigit()\n",
        "- isalpha()\n",
        "- isspace()\n",
        "- numeric()\n",
        "- ljust(width)\n",
        "- rjust(width)\n",
        "- cjust(width)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "trusted": true,
        "id": "nkRXM4BJG5tV",
        "colab_type": "code",
        "outputId": "b83daf37-3956-4d77-c9da-6ac7b1604c79",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        }
      },
      "source": [
        "# Python3 program to demonstarte \n",
        "# the str.format() method \n",
        "  \n",
        "# using format option in a simple string \n",
        "print (\"{}, A computer science portal for acropolis.\"\n",
        "                        .format(\"acropolis\")) \n",
        "  \n",
        "# using format option for a \n",
        "# value stored in a variable \n",
        "str = \"This article is written in {}\"\n",
        "print (str.format(\"Python\")) \n",
        "  \n",
        "# formatting a string using a numeric constant \n",
        "print (\"Hello, I am {} years old !\".format(20))  "
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "acropolis, A computer science portal for acropolis.\n",
            "This article is written in Python\n",
            "Hello, I am 20 years old !\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "trusted": false,
        "id": "m50gn_tsG5tb",
        "colab_type": "code",
        "outputId": "76b2f094-b561-4544-dc59-c400c521d037",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        }
      },
      "source": [
        "# Characters and their ASCII value\n",
        "\n",
        "x=68\n",
        "# print character corresponding to x \n",
        "print(chr(x))\n",
        "char='D'\n",
        "# print number corresponding to char\n",
        "print(ord(char))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "D\n",
            "68\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "trusted": true,
        "id": "b0mbEsRfG5tg",
        "colab_type": "code",
        "outputId": "a012a684-5f26-4d65-a69c-30b14698a4e1",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "# write code to print your name 10 times\n",
        "print('ACROPOLIS'*10)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "ACROPOLISACROPOLISACROPOLISACROPOLISACROPOLISACROPOLISACROPOLISACROPOLISACROPOLISACROPOLIS\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "trusted": true,
        "id": "HQhqPPfaG5tl",
        "colab_type": "code",
        "outputId": "128a86f6-fab5-41c2-c45f-0be50d8a6e93",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        }
      },
      "source": [
        "for i in range(5):\n",
        "    print(\"*\"*i)\n",
        "\n",
        "# new pattern program\n",
        "print(\"\\n\")\n",
        "for i in range(4,0,-1):\n",
        "  print(\"*\"*i)    "
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\n",
            "*\n",
            "**\n",
            "***\n",
            "****\n",
            "\n",
            "\n",
            "****\n",
            "***\n",
            "**\n",
            "*\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3-9RKU1psovu",
        "colab_type": "code",
        "outputId": "8fe9ea80-2d6b-46e9-ef2f-231030f11522",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 105
        }
      },
      "source": [
        "for i in range(1,6):\n",
        "  print(\" \"*(6-i),\"*\"*i) "
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "      *\n",
            "     **\n",
            "    ***\n",
            "   ****\n",
            "  *****\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "trusted": true,
        "id": "v5QAgvn8G5tp",
        "colab_type": "code",
        "outputId": "6c1274fe-0356-46c5-9218-476eaf14409e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "# use seperator and end with specific symbol\n",
        "a, b, c = 10, 20, 30\n",
        "print(a,b,c,sep=':',end=',')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "10:20:30,"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "trusted": true,
        "id": "IxLqu9XZG5tt",
        "colab_type": "code",
        "outputId": "e3a8267b-391c-4224-8733-09d2e82fd8be",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 87
        }
      },
      "source": [
        "for i in range(1,5):\n",
        "    print(\" \"*(5-i),\"*\"*i)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "     *\n",
            "    **\n",
            "   ***\n",
            "  ****\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "p29PsNILhUii",
        "colab_type": "text"
      },
      "source": [
        ""
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "trusted": false,
        "id": "GFIBWQUtG5tx",
        "colab_type": "code",
        "outputId": "9a4a11df-c26a-4a6b-86a0-e6d4b0b08a7c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "# unpack characters\n",
        "word = 'PYTHON'\n",
        "a,b,c,d,e,f = word\n",
        "print(a,b,c,d,e,f)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "P Y T H O N\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XOxjxinfG5t1",
        "colab_type": "text"
      },
      "source": [
        "### Format output"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab_type": "code",
        "id": "EJWEn5P4cfOd",
        "trusted": true,
        "outputId": "683a814b-0aa7-472b-e7d5-20b072bac8c0",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "x = 5 \n",
        "y = 10\n",
        "print('The value of x is {} and y is {}'.format(x,y))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "The value of x is 5 and y is 10\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "trusted": false,
        "id": "rohJ0RmQG5t6",
        "colab_type": "code",
        "outputId": "7e014ed8-e6d0-4592-9847-f212dae3a433",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "print('I like {0} and {1}'.format('ice cream','chocolate'))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "I like ice cream and chocolate\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "trusted": false,
        "id": "ePTsWKD2G5t-",
        "colab_type": "code",
        "outputId": "2db1ae32-fe91-4627-a365-0a75c7deb139",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "print('I like {1} and {0}'.format('ice cream','chocolate'))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "I like chocolate and ice cream\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "trusted": false,
        "id": "MHagJ4n_G5uE",
        "colab_type": "code",
        "outputId": "6f08fc85-4898-480c-fa53-6411e572e21c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "print('Hello {name}, {greeting}'.format(greeting = 'Good morning', name = 'Sachin !'))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Hello Sachin !, Good morning\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "liwzGLgJG5uJ",
        "colab_type": "text"
      },
      "source": [
        "### Task2\n",
        "#### Raman likes tea but he has coffee. Riya likes coffee but has tea. Write a program in python so that both can enjoy what they like."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "trusted": false,
        "id": "KLT5upfKG5uK",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# write your code after this line\n",
        "raman_has='coffee'\n",
        "riya_has='tea'\n",
        "temp=raman_has\n",
        "raman_has=riya_has\n",
        "riya_has=temp\n",
        "print(\"raman_has :{}\".format(raman))\n",
        "print(\"riya_has :{}\".format(riya))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "heading_collapsed": true,
        "id": "S2j-VmN9G5uN",
        "colab_type": "text"
      },
      "source": [
        "### Task3\n",
        "Write a program for following\n",
        "- Input: 'Python'\n",
        "- Output: 642"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "hidden": true,
        "trusted": true,
        "id": "VEgfNycFG5uO",
        "colab_type": "code",
        "outputId": "017824e8-2717-43e3-a098-d1f53a97b0bc",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "e,f,g,h,i,j='Python'\n",
        "s=ord(e)+ord(f)+ord(g)+ord(h)+ord(i)+ord(j)\n",
        "print(s)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "642\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DjUR0ktSG5uR",
        "colab_type": "text"
      },
      "source": [
        "# Working with math, calendar, random, datetime"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "trusted": true,
        "id": "y8UbqGZ1G5uS",
        "colab_type": "code",
        "outputId": "f8803f30-efe4-4047-af09-77866cf51a76",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 85
        }
      },
      "source": [
        "import math\n",
        "print(math.sqrt(9))\n",
        "print(math.floor(10.8))\n",
        "print (math.ceil(10.5))\n",
        "math.pi\n"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "3.0\n",
            "10\n",
            "11\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3.141592653589793"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 2
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "trusted": false,
        "id": "9Sofw03xG5uW",
        "colab_type": "code",
        "outputId": "0354b53e-3086-4d52-d67e-2adca9fc8b90",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        }
      },
      "source": [
        "import random\n",
        "x = random.random() # generate any random number between 0 and 1\n",
        "print(\"x = \", x)\n",
        "\n",
        "y = random.randint(5,20)# generate any random number between 5 and 20\n",
        "print(\"y = \", y)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "x =  0.9926331591882972\n",
            "y =  18\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "trusted": false,
        "id": "zJhrO4MyG5uZ",
        "colab_type": "code",
        "outputId": "ea741ecf-c362-400d-e300-48af69e9b34f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 85
        }
      },
      "source": [
        "import datetime\n",
        "\n",
        "date = datetime.datetime.now().date() # YYYY-MM-DD format\n",
        "year = datetime.datetime.now().year\n",
        "month = datetime.datetime.now().month\n",
        "day = datetime.datetime.now().day\n",
        "\n",
        "print(date)\n",
        "print(year)\n",
        "print(month)\n",
        "print(day)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "2020-01-09\n",
            "2020\n",
            "1\n",
            "9\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": false,
        "trusted": true,
        "id": "cq9pMSf4G5uc",
        "colab_type": "code",
        "outputId": "6f230d21-c0d5-48ec-bc19-ddf3569549dc",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 187
        }
      },
      "source": [
        "import calendar\n",
        "\n",
        "year = int(input(\"Enter Year : \"))\n",
        "month = int(input(\"Enter the Month : \"))\n",
        "\n",
        "print(calendar.month(year, month))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter Year : 2020\n",
            "Enter the Month : 1\n",
            "    January 2020\n",
            "Mo Tu We Th Fr Sa Su\n",
            "       1  2  3  4  5\n",
            " 6  7  8  9 10 11 12\n",
            "13 14 15 16 17 18 19\n",
            "20 21 22 23 24 25 26\n",
            "27 28 29 30 31\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-nTzI58dwwq-",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}