import React, { useEffect, useState } from "react";
import ObjectRepositoryForm from "../components/ObjectRepositoryForm";
import ObjectRepositoryTable from "../components/ObjectRepositoryTable";

export default function ObjectRepository() {
  const [objects, setObjects] = useState([]);
  const [editingObject, setEditingObject] = useState(null);

  // Fetch objects
  const fetchObjects = async () => {
    try {
      const res = await fetch("http://localhost:8000/object-repository/");
      const data = await res.json();
      setObjects(data);
    } catch (err) {
      console.error("Error fetching objects:", err);
    }
  };

  useEffect(() => {
    fetchObjects();
  }, []);

  const handleSave = async (obj) => {
    try {
      if (obj.id) {
        // update
        await fetch(`http://localhost:8000/object-repository/${obj.id}`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(obj),
        }); 
      } else {
        // create
        await fetch("http://localhost:8000/object-repository/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(obj),
        });
      }
      setEditingObject(null);
      fetchObjects();
    } catch (err) {
      console.error("Error saving object:", err);
    }
  };

  const handleDelete = async (id) => {
    if (!window.confirm("Delete this object?")) return;
    try {
      await fetch(`http://localhost:8000/object-repository/${id}`, {
        method: "DELETE",
      });
      fetchObjects();
    } catch (err) {
      console.error("Error deleting object:", err);
    }
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-6">Object Repository</h1>
      <ObjectRepositoryForm
        onSave={handleSave}
        editingObject={editingObject}
        onCancel={() => setEditingObject(null)}
      />
      <ObjectRepositoryTable
        objects={objects}
        onEdit={setEditingObject}
        onDelete={handleDelete}
      />
    </div>
  );
}
