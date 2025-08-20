import React, { useEffect, useState } from "react";

export default function GlobalVariablesPage() {
  // State management
  const [variables, setVariables] = useState([]);
  const [form, setForm] = useState({ key: "", value: "" });
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [searchTerm, setSearchTerm] = useState("");

  // Constants
  const API_URL = "http://localhost:8000/global-variables";

  // Fetch variables from backend
  const fetchVariables = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const res = await fetch(API_URL);
      if (!res.ok) throw new Error(`Failed to fetch variables: ${res.statusText}`);
      const data = await res.json();
      setVariables(data);
    } catch (err) {
      setError(err.message);
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchVariables();
  }, []);

  // Handle input change
  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
    setError(null); // Clear error when user types
  };

  // Save new variable
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Validation
    if (!form.key.trim()) {
      setError("Variable key is required");
      return;
    }
    if (!form.value.trim()) {
      setError("Variable value is required");
      return;
    }

    setIsLoading(true);
    setError(null);
    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });
      if (!res.ok) throw new Error("Failed to save variable");
      setForm({ key: "", value: "" });
      fetchVariables();
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  // Delete variable
  const handleDelete = async (id) => {
    if (!window.confirm("Are you sure you want to delete this variable?")) {
      return;
    }

    setIsLoading(true);
    setError(null);
    try {
      const res = await fetch(`${API_URL}/${id}`, {
        method: "DELETE"
      });
      if (!res.ok) throw new Error("Failed to delete variable");
      fetchVariables();
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  // Filter variables based on search term
  const filteredVariables = variables.filter(v => 
    v.key?.toLowerCase().includes(searchTerm.toLowerCase()) ||
    v.value?.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">Global Variables</h1>

      {/* Error Display */}
      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      {/* Search Input */}
      <input
        type="text"
        placeholder="Search variables..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        className="w-full p-2 mb-4 border rounded"
      />

      {/* Add Variable Form */}
      <form onSubmit={handleSubmit} className="space-y-4 mb-6">
        <input
          type="text"
          name="key"
          placeholder="Variable Key (e.g., GITHUB_URL)"
          value={form.key}
          onChange={handleChange}
          className="border p-2 w-full rounded focus:ring-2 focus:ring-blue-500"
          required
        />
        <input
          type="text"
          name="value"
          placeholder="Variable Value (e.g., https://github.com)"
          value={form.value}
          onChange={handleChange}
          className="border p-2 w-full rounded focus:ring-2 focus:ring-blue-500"
          required
        />
        <button
          type="submit"
          disabled={isLoading}
          className={`bg-blue-600 text-white px-4 py-2 rounded w-full
            ${isLoading ? 'opacity-50 cursor-not-allowed' : 'hover:bg-blue-700'}`}
        >
          {isLoading ? 'Saving...' : 'Save Variable'}
        </button>
      </form>

      {/* Loading Indicator */}
      {isLoading && (
        <div className="flex justify-center my-4">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500"></div>
        </div>
      )}

      {/* Variables Table */}
      <table className="min-w-full border">
        <thead>
          <tr className="bg-gray-100">
            <th className="p-2 border">Key</th>
            <th className="p-2 border">Value</th>
            <th className="p-2 border">Actions</th>
          </tr>
        </thead>
        <tbody>
          {filteredVariables.map((v) => (
            <tr key={v.id}>
              <td className="p-2 border">{v.key}</td>
              <td className="p-2 border">{v.value}</td>
              <td className="p-2 border">
                <button
                  onClick={() => handleDelete(v.id)}
                  disabled={isLoading}
                  className={`bg-red-600 text-white px-2 py-1 rounded
                    ${isLoading ? 'opacity-50 cursor-not-allowed' : 'hover:bg-red-700'}`}
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
          {filteredVariables.length === 0 && (
            <tr>
              <td colSpan="3" className="p-2 text-center text-gray-500">
                {searchTerm ? 'No matching variables found.' : 'No global variables found.'}
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}