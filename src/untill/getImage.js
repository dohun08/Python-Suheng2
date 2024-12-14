import axios from 'axios';

export const getData = async (item)=>{
    try {
      const res = await axios.get(`http://127.0.0.1:8000/api/data/${item}`, {
        responseType: 'blob' // 응답을 Blob 형식으로 받기
      });
    
      const imageObjectURL = URL.createObjectURL(res.data); 

      return(imageObjectURL);
    } catch (error) {
      console.log(error);
    }
  }