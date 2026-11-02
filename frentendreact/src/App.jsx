import { BrowserRouter, Routes, Route } from "react-router-dom";

import TopHeader from "./components/TopHeader";
import Home from "./pages/Home";

function App() {
    return (
        <BrowserRouter>
            <TopHeader />

            <Routes>
                <Route path="/" element={<Home />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;