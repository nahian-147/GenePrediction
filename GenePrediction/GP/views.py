from django.shortcuts import render
import numpy as np
import pandas as pd
from Bio.Seq import Seq
from Bio import SeqIO
from .ORF import findPotentialCodingSegments

def home(request):
	return render(request,'GP/home.html')

def predict(request):
    record_iterator = SeqIO.parse("/home/nahian/Desktop/GenePrediction/GenePrediction/GP/NZ_GG770409.fna", "fasta")
    record1 = next(record_iterator)
    sq = str(record1.seq)
    stopList = [i for i in range(len(sq)) if (sq.startswith('TGA',i) or sq.startswith('TAG',i) or sq.startswith('TAA',i))]
    orfs = findPotentialCodingSegments(sq,stopList)

    context = {
	    'orfs':orfs
    }
    return render(request,'GP/Genes.html',context)
    