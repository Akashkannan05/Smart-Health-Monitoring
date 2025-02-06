import './App.css'
import { Chatbot } from './Components/Chatbot/Chatbot'
import { Navbar } from './Components/Navbar/Navbar'
import { Home } from './Pages/Home/Home'
import { Profile } from './Pages/Home/Profile/Profile'

function App() {

  return (
    <>
    <Chatbot/> <Navbar /> <Home/>
      {/* <Profile/> */}
    </>
  )
}

export default App
