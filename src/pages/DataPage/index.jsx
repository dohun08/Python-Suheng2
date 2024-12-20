import styled from 'styled-components';
import CarImage from '../../assets/carimage.jpeg';
import {Link} from 'react-router-dom';
import { useEffect, useState } from 'react';
import { getData } from '../../untill/getImage';
import Map from '../../assets/map.svg';

export default function DataPage(){
  const [url, seturl] = useState();
  const [url2, seturl2] = useState();
  const [isLoading, setIsLoading] = useState(true);
  useEffect(()=>{
    get();
  }, [])
  const get = async ()=>{
    try {
      const address = await getData("/api/graph");
      const address2 = await getData("/api/graph2");
      seturl(address);
      seturl2(address2);
    } catch (error) {
      console.log(error);
    }finally{
      setIsLoading(false);
    }
  }
  if(isLoading) return <p>로딩중</p>
    return(
        <Container>
            <Black />
            <Link to={'/rank'}><Btn>돌아가기</Btn></Link>
                <Main>
                    <img src={url} alt='graph' width={'100%'}/>
                </Main>
                <Main>
                <img src={Map} alt='map' width={'100%'}/>
                <BoxBox>
            <p>이용률 낮음</p>
            <Box style={{ backgroundColor: '#1E90FF' }} />
            <Box style={{ backgroundColor: '#00BFFF' }} />
            <Box style={{ backgroundColor: '#40E0D0' }} />
            <Box style={{ backgroundColor: '#00FF7F' }} />
            <Box style={{ backgroundColor: '#87CEEB' }} />
            <Box style={{ backgroundColor: '#FFA500' }} />
            <Box style={{ backgroundColor: '#FF4500' }} />
            <Box style={{ backgroundColor: '#FF0000' }} />
            <Box style={{ backgroundColor: '#B22222' }} />
            <Box style={{ backgroundColor: '#460000' }} />
            <p>이용률 높음</p>
        </BoxBox>
                </Main>
                <Main>
                <img src={url2} alt='graph' width={'100%'}/>
                <p>서울, 부산, 대구, 인천, 경기지역빼고는 모두 5%미만</p>
                </Main>
        </Container>
    )
}
export const Btn = styled.button`
z-index: 2;
  background-color: white;
  padding: 15px 20px;
  outline: none;
  position: absolute;
  left:20px;
  top: 20px;
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
const Container = styled.div`
  display: flex;
  flex-flow: row wrap;
  justify-content: space-around;
  align-items: center;
  width: 100vw;
  height: 100vh;
  background: url(${CarImage}) no-repeat;
  background-size: cover;
`
const Black = styled.div`
background-color: rgb(0, 0, 0, 0.5);
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
z-index: 1;
`
const Main = styled.main`
    background-color: white;
    width: 30%;
    padding: 20px 18px;
    z-index: 2;
    border-radius: 8px;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
`
const Box = styled.div`
    width: 10px;
    height: 10px;
    border: 1px solid black;
`;

// Styled component for the container
const BoxBox = styled.div`
    margin-top: 10px;
    align-items: center;
    display: flex;
    justify-content: space-between;
    gap: 5px;
    font-size: 14px;
`;