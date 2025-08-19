import { useState, useEffect } from "react";

const STATUS_COLORS = {
  pending: "bg-yellow-100 text-yellow-800",
  running: "bg-blue-100 text-blue-800",
  passed: "bg-green-100 text-green-800",
  failed: "bg-red-100 text-red-800",
};

export default function TestManager() {
  const [testCases, setTestCases] = useState([]);
  const [newTestCase, setNewTestCase] = useState({
    name: "",
    description: "",
    status: "pending",
  });
  const [loading, setLoading] = useState(false);
  const [tab, setTab] = useState("list");

  useEffect(() => {
    fetch("http://localhost:8000/testcases")
      .then((res) => res.json())
      .then(setTestCases)
      .catch(console.error);
  }, []);

  const createTestCase = async () => {
    if (!newTestCase.name.trim()) return;

    setLoading(true);
    try {
      const res = await fetch("http://localhost:8000/testcases", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newTestCase),
      });
      const data = await res.json();
      setTestCases([...testCases, data]);
      setNewTestCase({ name: "", description: "", status: "pending" });
      setTab("list");
    } catch (err) {
      console.error(err);
    }
    setLoading(false);
  };

  const formatDate = (dateStr) => {
    const date = new Date(dateStr);
    return date.toLocaleString();
  };

  return (
    <div className="max-w-5xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6">🧪 Test Cases</h1>

      {/* Tabs */}
      <div className="flex gap-4 mb-6">
        <button
          className={`px-4 py-2 rounded-md border ${
            tab === "list"
              ? "bg-blue-600 text-white border-blue-600"
              : "bg-white text-gray-700 border-gray-300"
          }`}
          onClick={() => setTab("list")}
        >
          All Test Cases
        </button>
        <button
          className={`px-4 py-2 rounded-md border ${
            tab === "create"
              ? "bg-blue-600 text-white border-blue-600"
              : "bg-white text-gray-700 border-gray-300"
          }`}
          onClick={() => setTab("create")}
        >
          Create Test Case
        </button>
      </div>

      {/* List View */}
      {tab === "list" && (
        <div className="grid gap-6 md:grid-cols-2">
          {testCases.length === 0 ? (
            <p className="text-gray-500">No test cases found.</p>
          ) : (
            testCases.map((tc) => (
              <div
                key={tc.id}
                className="border rounded-md p-4 shadow-sm bg-white"
              >
                <div className="flex justify-between items-center mb-2">
                  <h2 className="text-lg font-semibold">{tc.name}</h2>
                  <span
                    className={`text-xs font-semibold px-2 py-1 rounded-full ${STATUS_COLORS[tc.status]}`}
                  >
                    {tc.status}
                  </span>
                </div>
                <p className="text-gray-600 mb-2">{tc.description || "-"}</p>
                <div className="text-xs text-gray-400">
                  Created: {formatDate(tc.created_at)}
                </div>
                <div className="text-xs text-gray-400">
                  Updated: {tc.updated_at ? formatDate(tc.updated_at) : "-"}
                </div>
                {/* TODO: Add Edit/Delete buttons here */}
              </div>
            ))
          )}
        </div>
      )}

      {/* Create Form */}
      {tab === "create" && (
        <div className="max-w-lg bg-white p-6 rounded-md shadow-md">
          <h2 className="text-xl font-semibold mb-4">Create New Test Case</h2>
          <div className="space-y-4">
            <div>
              <label className="block mb-1 font-medium">Name</label>
              <input
                type="text"
                className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="Test case name"
                value={newTestCase.name}
                onChange={(e) =>
                  setNewTestCase({ ...newTestCase, name: e.target.value })
                }
              />
            </div>
            <div>
              <label className="block mb-1 font-medium">Description</label>
              <textarea
                className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="Description (optional)"
                rows={3}
                value={newTestCase.description}
                onChange={(e) =>
                  setNewTestCase({ ...newTestCase, description: e.target.value })
                }
              />
            </div>
            <div>
              <label className="block mb-1 font-medium">Status</label>
              <select
                className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                value={newTestCase.status}
                onChange={(e) =>
                  setNewTestCase({ ...newTestCase, status: e.target.value })
                }
              >
                <option value="pending">Pending</option>
                <option value="running">Running</option>
                <option value="passed">Passed</option>
                <option value="failed">Failed</option>
              </select>
            </div>
            <button
              onClick={createTestCase}
              disabled={loading}
              className={`w-full py-2 rounded-md text-white ${
                loading ? "bg-gray-400" : "bg-blue-600 hover:bg-blue-700"
              }`}
            >
              {loading ? "Creating..." : "Create Test Case"}
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
