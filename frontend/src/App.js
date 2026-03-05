import React, { useEffect, useState } from "react";
import { getSources, createSource, updateSource, deleteSource } from "./api";

function App() {
    const [sources, setSources] = useState([]);
    const [name, setName] = useState("");
    const [url, setUrl] = useState("");

    const fetchSources = async () => {
        const res = await getSources();
        setSources(res.data);
    };

    useEffect(() => {
        fetchSources();
    }, []);

    const handleAdd = async () => {
        await createSource({ name, url });
        setName(""); setUrl("");
        fetchSources();
    };

    const handleDelete = async (id) => {
        await deleteSource(id);
        fetchSources();
    };

    return (
        <div style={{ padding: "20px" }}>
            <h1>News Sources</h1>
            <input placeholder="Name" value={name} onChange={e => setName(e.target.value)} />
            <input placeholder="URL" value={url} onChange={e => setUrl(e.target.value)} />
            <button onClick={handleAdd}>Add Source</button>

            <ul>
                {sources.map(s => (
                    <li key={s.id}>
                        {s.name} - {s.url}
                        <button onClick={() => handleDelete(s.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;