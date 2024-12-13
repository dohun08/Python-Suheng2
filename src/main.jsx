import { createRoot } from 'react-dom/client'
import App from './App.jsx'

import {
  BrowserRouter,
  Routes,
  Route
}from 'react-router-dom';

import Rank from './pages/RankingPage';
import Data from './pages/DataPage'
createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <Routes>
      <Route path='/' element={<App />}></Route>
      <Route path='/rank' element={<Rank />}></Route>
      <Route path='/data' element={<Data />}></Route>
    </Routes>
  </BrowserRouter>
)
