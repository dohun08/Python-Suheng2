import styled from 'styled-components';
import CarImage from '../../assets/carimage.jpeg';
import {Link} from 'react-router-dom';
import axios from 'axios'
import { useEffect, useState } from 'react';

export default function Ranking(){
    const [isLoading, setIsLoading] = useState(true);
    const [data, setData] = useState();
    useEffect(()=>{
        getData();
    }, [])
    const getData = async ()=>{
        try{
            const res = await axios.get('http://127.0.0.1:8000/api/rank')
            console.log(res.data);
            setData(res.data);
        }catch(error){
            console.log(error);
        }finally{
            setIsLoading(false);
        }
    }
    
    if(isLoading){
        return(
            <p>로딩중</p>
        )
    }

    return(
            <Container>
                <Lk to={'/'}><Btn>돌아가기</Btn></Lk>
                <Black />
                <Main>
                    <h1>랭킹</h1>
                    <MainBox>
                    {data.map((item, index)=>{
                        return(
                            <Box key={index}>
                                <p>{index+1} 위 : {item.name}</p>
                                <p>{item.value}명</p>
                            </Box>
                        )
                    })}
                    </MainBox>
                </Main>
                <Lk to={'/data'}><Btn>자료보기</Btn></Lk>
            </Container>
    )
}
const Lk = styled(Link)`
z-index: 2;

`
export const Btn = styled.button`
z-index: 2;
  background-color: white;
  padding: 15px 20px;
  outline: none;
  border: none;
  font-size: 20px;
  font-weight: 700;
  border-radius: 20px;
  cursor: pointer;
  transition: 0.2s;
  &:hover{
    background-color: #e7e7e7;
  }
  &:active{
    background-color: #d2d2d2;
  }
`
export const Black = styled.div`
background-color: rgb(0, 0, 0, 0.5);
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
z-index: 1;
`
export const Container = styled.div`
  display: flex;
  flex-flow: row wrap;
  justify-content: space-around;
  align-items: center;
  width: 100vw;
  height: 100vh;
  background: url(${CarImage}) no-repeat;
  background-size: cover;
`
const Main = styled.main`
    background-color: white;
    width: 40%;
    padding: 10px;
    z-index: 2;
    border-radius: 8px;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
`
const Box = styled.div`
    width: 100%;
    font-size: 18px;
    background-color: #e5e5e5;
    display: flex;
    border-radius: 8px;
    padding: 5px 15px;
    margin-bottom: 8px;
    justify-content: space-between;
`
const MainBox = styled.div`
    width: 85%;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    & > :nth-of-type(1){
        background-color: #f05b5b;
        font-weight: 700;
        padding: 10px 15px;
        font-size: 20px;
    }
    & > :nth-of-type(2){
        background-color: #e9ee67;
        padding: 10px 15px;
        font-weight: 700;
        font-size: 20px;
    }
    & > :nth-of-type(3){
        background-color: #588df7;
        padding: 10px 15px;
        font-weight: 700;
        font-size: 20px;
    }
`