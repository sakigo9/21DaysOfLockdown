function pickingNumbers(a) {
    a.sort((a,b)=>a-b)
    let temp=0,res=0;
    for(let i=0;i<a.length;i++){
        for(let j=i+1;j<a.length;j++){
            if(Math.abs(a[i]-a[j])<=1){
                temp++
            }
            if(temp>res) res=Math.max(res,temp)
        }
        temp=0;
    }
  return res+1
}
