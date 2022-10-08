function equalizeArray(arr) {
    let obj={}
    for(let i of arr){
        if(obj[i]){
           obj[i]++ 
        }else{
            obj[i]=1
        }
    }
    
    let res=0;
    for(let key in obj){
        console.log(key," - ",obj[key])
        res=Math.max(res,obj[key])
    }
    return arr.length-res
}
