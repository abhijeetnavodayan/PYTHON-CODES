d={"X":[70,80,90,68,59],"Y":[70,80,90,68,59],"Z":[70,80,90,68,59],"B":[70,80,90,68,59],"A":[70,80,90,68,59]}
for row in zip(*([k]+(v) for k,v in sorted(d.items()))):
    print(*row,sep="\t")