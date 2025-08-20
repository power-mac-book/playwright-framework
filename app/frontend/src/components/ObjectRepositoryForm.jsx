import React, { useState, useEffect } from "react";

export default function ObjectRepositoryForm({ onSave, editingObject, onCancel }) {
  const [form, setForm] = useState({
    name: "",
    locator_type: "css",
    locator_value: "",
    description: "",
    application: "",
  });

  useEffect(() => {
    if (editingObject) {
      setForm(editingObject);
    }
  }, [editingObject]);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSave(form);
    setForm({
      name: "",
      locator_type: "css",
      locator_value: "",
      description: "",
      application: "",
    });
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white p-4 rounded shadow mb-6">
      <div className="grid grid-cols-2 gap-4">
        <input
          name="name"
          placeholder="Object Name"
          value={form.name}
          onChange={handleChange}
          className="border p-2 rounded"
          required
        />
        <select
          name="locator_type"
          value={form.locator_type}
          onChange={handleChange}
          className="border p-2 rounded"
        >
          <option value="css">CSS</option>
          <option value="xpath">XPath</option>
          <option value="id">ID</option>
          <option value="name">Name</option>
        </select>
        <input
          name="locator_value"
          placeholder="Locator Value"
          value={form.locator_value}
          onChange={handleChange}
          className="border p-2 rounded col-span-2"
          required
        />
        <input
          name="application"
          placeholder="Application"
          value={form.application}
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          name="description"
          placeholder="Description"
          value={form.description}
          onChange={handleChange}
          className="border p-2 rounded"
        />
      </div>
      <div className="flex gap-2 mt-4">
        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          {editingObject ? "Update" : "Add"}
        </button>
        {editingObject && (
          <button
            type="button"
            onClick={onCancel}
            className="bg-gray-400 text-white px-4 py-2 rounded hover:bg-gray-500"
          >
            Cancel
          </button>
        )}
      </div>
    </form>
  );
}
