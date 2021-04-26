import axios from "axios";
import { useEffect, useState } from "react";
import { DOMAIN, getSharedData } from "./utils";

import "./App.css";

function App() {
    const [sharedData, setSharedData] = useState({ isLoaded: false });

    useEffect(() => {
        getSharedData().then((data) => {
            console.log(data);
            setSharedData({ ...data, isLoaded: true });
        });
    }, []);

    return (
        <div className="App">
            <header className="App-header">
                <p>Hello!</p>
                <Firstname {...sharedData} />
                <Message {...sharedData} />
            </header>
        </div>
    );
}

const Firstname = () => {
    const [firstName, setFirstname] = useState(null);

    useEffect(() => {
        axios.get(`${DOMAIN}/api/firstname/`).then((res) => {
            const { data } = res;
            if (data.first_name) setFirstname(data.first_name);
        });
    }, []);

    if (!firstName) return <div>Loading ....</div>;

    return <div>I am {firstName}</div>;
};

const Message = ({ isLoaded, message }) => {
    if (!isLoaded) return null;
    return <div>{message}</div>;
};

export default App;
