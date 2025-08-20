import React from "react";

export default function ObjectRepositoryTable({ objects, onEdit, onDelete }) {
       const safeObjects = Array.isArray(objects) ? objects : [];
    return (
    <table className="w-full bg-white shadow rounded">
      <thead className="bg-gray-200">
        <tr>
          <th className="p-2 text-left">Name</th>
          <th className="p-2 text-left">Locator Type</th>
          <th className="p-2 text-left">Locator Value</th>
          <th className="p-2 text-left">Application</th>
          <th className="p-2 text-left">Description</th>
          <th className="p-2 text-left">Actions</th>
        </tr>
      </thead>
      <tbody>
         {safeObjects.length === 0 ? (
            <tr>
              <td colSpan="4" className="text-center p-4 text-gray-500">
                No objects found
              </td>
            </tr>
          ) : (
        safeObjects.map((obj) => (
          <tr key={obj.id} className="border-t">
            <td className="p-2">{obj.name}</td>
            <td className="p-2">{obj.locator_type}</td>
            <td className="p-2">{obj.locator_value}</td>
            <td className="p-2">{obj.application}</td>
            <td className="p-2">{obj.description}</td>
            <td className="p-2 flex gap-2">
              <button
                onClick={() => onEdit(obj)}
                className="bg-yellow-500 text-white px-2 py-1 rounded hover:bg-yellow-600"
              >
                Edit
              </button>
              <button
                onClick={() => onDelete(obj.id)}
                className="bg-red-500 text-white px-2 py-1 rounded hover:bg-red-600"
              >
                Delete
              </button>
            </td>
          </tr>
        ))
    )}
      </tbody>
    </table>
  );
}
