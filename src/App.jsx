import styled from 'styled-components';
import CarImage from './assets/carimage.jpeg';
import {Link} from 'react-router-dom';
function App() {

  return (
    <Container>
      <Black />
      <Main>
        <Head>대한민국 대중교통 이용인원 현황</Head>
        <Link to={'/rank'}><Btn>보러가기</Btn></Link>
      </Main>
    </Container>
  )
}

export default App
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
  justify-content: center;
  align-items: center;
  width: 100vw;
  height: 100vh;
  background: url(${CarImage}) no-repeat;
  background-size: cover;
`
export const Main = styled.div`
display: flex;
justify-content: center;
align-items: center;
flex-direction: column;
  & > *{
    margin-bottom: 30px;
  }
  z-index: 2;
`
export const Head = styled.h1`
  color: white;
  font-size: 50px;
`
export const Btn = styled.button`
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