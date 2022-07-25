#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 22:49:24 2022

@author: tharuns
"""
#create block chain

import datetime
import hashlib
import json 
from flask import Flask,jsonify


#building block chain 
class BlockChain:
    def _init_(self):
        self.chain=[]
        self.createBlock(proof=1,previousHash='0')

    def createBlock(self,proof,previousHash):
        block ={
            'index':len(self.chain)+1,
            'timeStamp':str(datetime.datetime().now()),
            'proof':proof,
            'data':'',
            'previousHash':previousHash
            
            }
        self.chain.append(block);
        return block;
    
    def getPreviousBlck(self):
       return self.chain[-1]
   
    
   #make sure the hashcode is having 0000 in front
    def proof_of_work(self,previousProof):
        new_poof=1
        check_proof=False
        
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previousProof**2).encode()).hexdigest()
            if hash_operation[:4]=='0000':
                check_proof = True
            else:
                new_proof +=1
        return new_proof
    
    def hashfn(self,block):
         encoded_block = json.dumps(block, sort_keys=True).encode();
         return hashlib.sha256(encoded_block).hexdigest()
     
     def isChainValid(self,chain):
         previousBlock=chain[0];
         block_index=1;
         
         while block_index<len(chain):
             block = chain[block_index]
             if block['previousHash'] !=self.hash(previous_block):
                 return False
             previousProof=previousBlock['proof']
             proof=block['proof']
             hash_operation = hashlib.sha256(str(proof**2 - previousProof**2).encode()).hexdigest()
             if hash_operation[:4]!='0000':
                 return False
             previousBlock=block
             block_index+=1
             
        return True
         
        
                    