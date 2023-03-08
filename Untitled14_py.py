{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO0FlJOCe/fbHdPckwDCRAz",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Alagammaipl/BizcardX/blob/main/Untitled14_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install easyocr"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J7rnOW7PFo46",
        "outputId": "6fbe211a-8d56-44be-a211-a148e38e2d81"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting easyocr\n",
            "  Downloading easyocr-1.6.2-py3-none-any.whl (2.9 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.9/2.9 MB\u001b[0m \u001b[31m50.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: numpy in /usr/local/lib/python3.8/dist-packages (from easyocr) (1.22.4)\n",
            "Collecting pyclipper\n",
            "  Downloading pyclipper-1.3.0.post4-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl (619 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m619.2/619.2 KB\u001b[0m \u001b[31m45.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting python-bidi\n",
            "  Downloading python_bidi-0.4.2-py2.py3-none-any.whl (30 kB)\n",
            "Requirement already satisfied: PyYAML in /usr/local/lib/python3.8/dist-packages (from easyocr) (6.0)\n",
            "Collecting opencv-python-headless<=4.5.4.60\n",
            "  Downloading opencv_python_headless-4.5.4.60-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (47.6 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m47.6/47.6 MB\u001b[0m \u001b[31m16.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: Shapely in /usr/local/lib/python3.8/dist-packages (from easyocr) (2.0.1)\n",
            "Collecting ninja\n",
            "  Downloading ninja-1.11.1-py2.py3-none-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (145 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m146.0/146.0 KB\u001b[0m \u001b[31m16.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: Pillow in /usr/local/lib/python3.8/dist-packages (from easyocr) (8.4.0)\n",
            "Requirement already satisfied: scipy in /usr/local/lib/python3.8/dist-packages (from easyocr) (1.10.1)\n",
            "Requirement already satisfied: scikit-image in /usr/local/lib/python3.8/dist-packages (from easyocr) (0.19.3)\n",
            "Requirement already satisfied: torch in /usr/local/lib/python3.8/dist-packages (from easyocr) (1.13.1+cu116)\n",
            "Requirement already satisfied: torchvision>=0.5 in /usr/local/lib/python3.8/dist-packages (from easyocr) (0.14.1+cu116)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.8/dist-packages (from torchvision>=0.5->easyocr) (2.25.1)\n",
            "Requirement already satisfied: typing-extensions in /usr/local/lib/python3.8/dist-packages (from torchvision>=0.5->easyocr) (4.5.0)\n",
            "Requirement already satisfied: six in /usr/local/lib/python3.8/dist-packages (from python-bidi->easyocr) (1.15.0)\n",
            "Requirement already satisfied: PyWavelets>=1.1.1 in /usr/local/lib/python3.8/dist-packages (from scikit-image->easyocr) (1.4.1)\n",
            "Requirement already satisfied: networkx>=2.2 in /usr/local/lib/python3.8/dist-packages (from scikit-image->easyocr) (3.0)\n",
            "Requirement already satisfied: imageio>=2.4.1 in /usr/local/lib/python3.8/dist-packages (from scikit-image->easyocr) (2.9.0)\n",
            "Requirement already satisfied: tifffile>=2019.7.26 in /usr/local/lib/python3.8/dist-packages (from scikit-image->easyocr) (2023.2.28)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.8/dist-packages (from scikit-image->easyocr) (23.0)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.8/dist-packages (from requests->torchvision>=0.5->easyocr) (2.10)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.8/dist-packages (from requests->torchvision>=0.5->easyocr) (2022.12.7)\n",
            "Requirement already satisfied: chardet<5,>=3.0.2 in /usr/local/lib/python3.8/dist-packages (from requests->torchvision>=0.5->easyocr) (4.0.0)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.8/dist-packages (from requests->torchvision>=0.5->easyocr) (1.26.14)\n",
            "Installing collected packages: pyclipper, ninja, python-bidi, opencv-python-headless, easyocr\n",
            "  Attempting uninstall: opencv-python-headless\n",
            "    Found existing installation: opencv-python-headless 4.7.0.72\n",
            "    Uninstalling opencv-python-headless-4.7.0.72:\n",
            "      Successfully uninstalled opencv-python-headless-4.7.0.72\n",
            "Successfully installed easyocr-1.6.2 ninja-1.11.1 opencv-python-headless-4.5.4.60 pyclipper-1.3.0.post4 python-bidi-0.4.2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "! pip install streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TAxnmVYjFvHD",
        "outputId": "b547c57e-e6f4-44e6-8474-e29f4eb1f4a1"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting streamlit\n",
            "  Downloading streamlit-1.19.0-py2.py3-none-any.whl (9.6 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.6/9.6 MB\u001b[0m \u001b[31m61.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: toml in /usr/local/lib/python3.8/dist-packages (from streamlit) (0.10.2)\n",
            "Collecting validators>=0.2\n",
            "  Downloading validators-0.20.0.tar.gz (30 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Requirement already satisfied: requests>=2.4 in /usr/local/lib/python3.8/dist-packages (from streamlit) (2.25.1)\n",
            "Requirement already satisfied: pandas>=0.25 in /usr/local/lib/python3.8/dist-packages (from streamlit) (1.3.5)\n",
            "Requirement already satisfied: importlib-metadata>=1.4 in /usr/local/lib/python3.8/dist-packages (from streamlit) (6.0.0)\n",
            "Collecting pydeck>=0.1.dev5\n",
            "  Downloading pydeck-0.8.0-py2.py3-none-any.whl (4.7 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4.7/4.7 MB\u001b[0m \u001b[31m61.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: packaging>=14.1 in /usr/local/lib/python3.8/dist-packages (from streamlit) (23.0)\n",
            "Collecting blinker>=1.0.0\n",
            "  Downloading blinker-1.5-py2.py3-none-any.whl (12 kB)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.8/dist-packages (from streamlit) (2.8.2)\n",
            "Collecting watchdog\n",
            "  Downloading watchdog-2.3.1-py3-none-manylinux2014_x86_64.whl (80 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m80.6/80.6 KB\u001b[0m \u001b[31m8.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: cachetools>=4.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (5.3.0)\n",
            "Requirement already satisfied: tzlocal>=1.1 in /usr/local/lib/python3.8/dist-packages (from streamlit) (1.5.1)\n",
            "Collecting semver\n",
            "  Downloading semver-2.13.0-py2.py3-none-any.whl (12 kB)\n",
            "Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (8.4.0)\n",
            "Requirement already satisfied: altair>=3.2.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (4.2.2)\n",
            "Collecting rich>=10.11.0\n",
            "  Downloading rich-13.3.2-py3-none-any.whl (238 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m238.7/238.7 KB\u001b[0m \u001b[31m24.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: tornado>=6.0.3 in /usr/local/lib/python3.8/dist-packages (from streamlit) (6.2)\n",
            "Collecting pympler>=0.9\n",
            "  Downloading Pympler-1.0.1-py3-none-any.whl (164 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m164.8/164.8 KB\u001b[0m \u001b[31m15.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: numpy in /usr/local/lib/python3.8/dist-packages (from streamlit) (1.22.4)\n",
            "Collecting gitpython!=3.1.19\n",
            "  Downloading GitPython-3.1.31-py3-none-any.whl (184 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m184.3/184.3 KB\u001b[0m \u001b[31m14.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: typing-extensions>=3.10.0.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (4.5.0)\n",
            "Requirement already satisfied: protobuf<4,>=3.12 in /usr/local/lib/python3.8/dist-packages (from streamlit) (3.19.6)\n",
            "Requirement already satisfied: click>=7.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (8.1.3)\n",
            "Requirement already satisfied: pyarrow>=4.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (9.0.0)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.8/dist-packages (from altair>=3.2.0->streamlit) (0.4)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.8/dist-packages (from altair>=3.2.0->streamlit) (0.12.0)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.8/dist-packages (from altair>=3.2.0->streamlit) (4.3.3)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.8/dist-packages (from altair>=3.2.0->streamlit) (3.1.2)\n",
            "Collecting gitdb<5,>=4.0.1\n",
            "  Downloading gitdb-4.0.10-py3-none-any.whl (62 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 KB\u001b[0m \u001b[31m5.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.8/dist-packages (from importlib-metadata>=1.4->streamlit) (3.15.0)\n",
            "Requirement already satisfied: pytz>=2017.3 in /usr/local/lib/python3.8/dist-packages (from pandas>=0.25->streamlit) (2022.7.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.8/dist-packages (from python-dateutil->streamlit) (1.15.0)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.8/dist-packages (from requests>=2.4->streamlit) (1.26.14)\n",
            "Requirement already satisfied: chardet<5,>=3.0.2 in /usr/local/lib/python3.8/dist-packages (from requests>=2.4->streamlit) (4.0.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.8/dist-packages (from requests>=2.4->streamlit) (2022.12.7)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.8/dist-packages (from requests>=2.4->streamlit) (2.10)\n",
            "Collecting pygments<3.0.0,>=2.13.0\n",
            "  Downloading Pygments-2.14.0-py3-none-any.whl (1.1 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.1/1.1 MB\u001b[0m \u001b[31m11.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting markdown-it-py<3.0.0,>=2.2.0\n",
            "  Downloading markdown_it_py-2.2.0-py3-none-any.whl (84 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m84.5/84.5 KB\u001b[0m \u001b[31m6.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: decorator>=3.4.0 in /usr/local/lib/python3.8/dist-packages (from validators>=0.2->streamlit) (4.4.2)\n",
            "Collecting smmap<6,>=3.0.1\n",
            "  Downloading smmap-5.0.0-py3-none-any.whl (24 kB)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.8/dist-packages (from jinja2->altair>=3.2.0->streamlit) (2.1.2)\n",
            "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.8/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (22.2.0)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.8/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (0.19.3)\n",
            "Requirement already satisfied: importlib-resources>=1.4.0 in /usr/local/lib/python3.8/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (5.12.0)\n",
            "Collecting mdurl~=0.1\n",
            "  Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)\n",
            "Building wheels for collected packages: validators\n",
            "  Building wheel for validators (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for validators: filename=validators-0.20.0-py3-none-any.whl size=19581 sha256=e7a7e5a4043988cc1581dcfcf04e76159c9df14639e3012133ac64781c4a4a6f\n",
            "  Stored in directory: /root/.cache/pip/wheels/19/09/72/3eb74d236bb48bd0f3c6c3c83e4e0c5bbfcbcad7c6c3539db8\n",
            "Successfully built validators\n",
            "Installing collected packages: watchdog, validators, smmap, semver, pympler, pygments, mdurl, blinker, pydeck, markdown-it-py, gitdb, rich, gitpython, streamlit\n",
            "  Attempting uninstall: pygments\n",
            "    Found existing installation: Pygments 2.6.1\n",
            "    Uninstalling Pygments-2.6.1:\n",
            "      Successfully uninstalled Pygments-2.6.1\n",
            "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "ipython 7.9.0 requires jedi>=0.10, which is not installed.\u001b[0m\u001b[31m\n",
            "\u001b[0mSuccessfully installed blinker-1.5 gitdb-4.0.10 gitpython-3.1.31 markdown-it-py-2.2.0 mdurl-0.1.2 pydeck-0.8.0 pygments-2.14.0 pympler-1.0.1 rich-13.3.2 semver-2.13.0 smmap-5.0.0 streamlit-1.19.0 validators-0.20.0 watchdog-2.3.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Bb7QZXcWFgkX",
        "outputId": "cdce669a-e2b6-4e96-c64a-4d0098bec0fa"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:root:\n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.8/dist-packages/ipykernel_launcher.py [ARGUMENTS]\n",
            "2023-03-08 11:59:56.796 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.8/dist-packages/ipykernel_launcher.py [ARGUMENTS]\n"
          ]
        }
      ],
      "source": [
        "import streamlit as st\n",
        "import easyocr as ocr\n",
        "import sqlite3\n",
        "\n",
        "uploaded_file = st.file_uploader(\"Upload a business card image\", type=[\"jpg\", \"jpeg\", \"png\"])\n",
        "if st.button(\"Extract Information\"):\n",
        "    if uploaded_file is not None:\n",
        "        image = uploaded_file.read()\n",
        "        reader = ocr.Reader(['en'])\n",
        "        results = reader.readtext(image)      \n",
        "        st.write(\"Extracted Information:\")\n",
        "        table_data = [[result[0], result[1]] for result in results]\n",
        "        st.table(table_data) \n",
        "        conn = sqlite3.connect('business_cards.db')\n",
        "        c = conn.cursor()\n",
        "        c.execute('CREATE TABLE IF NOT EXISTS business_cards (id INTEGER PRIMARY KEY, image BLOB, name TEXT, email TEXT, phone TEXT)')\n",
        "        name = \"\"\n",
        "        email = \"\"\n",
        "        phone = \"\"\n",
        "        for result in results:\n",
        "            if \"name\" in result[1].lower():\n",
        "                name = result[1].split(\"name\")[-1].strip()\n",
        "            elif \"email\" in result[1].lower():\n",
        "                email = result[1].split(\"email\")[-1].strip()\n",
        "            elif \"phone\" in result[1].lower():\n",
        "                phone = result[1].split(\"phone\")[-1].strip()\n",
        "        c.execute(\"INSERT INTO business_cards (image, name, email, phone) VALUES (?, ?, ?, ?)\", (sqlite3.Binary(image), name, email, phone))\n",
        "        conn.commit()\n",
        "        conn.close()\n",
        "    else:\n",
        "        st.write(\"Please upload an image before extracting information.\")"
      ]
    }
  ]
}