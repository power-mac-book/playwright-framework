import { useState } from 'react';
import StepList from '../components/StepList';
import TestControls from '../components/TestControl';
import TestResult from '../components/TestResult';
// import axios from 'axios';

export default function TestDesignerPage() {
  const [description, setDescription] = useState('');
  const [steps, setSteps] = useState([{ action: 'goto', selector: '', value: '' }]);
  const [result, setResult] = useState('');

  const addStep = () => setSteps([...steps, { action: 'click', selector: '', value: '' }]);
  const updateStep = (index, field, value) => {
    const newSteps = [...steps];
    newSteps[index][field] = value;
    setSteps(newSteps);
  };
  const removeStep = (index) => setSteps(steps.filter((_, i) => i !== index));

   const runTest = async () => {
     try {
  //     const res = await axios.post('http://localhost:8000/run-test', { description, steps });
  //     setResult(res.data.message);
     } catch (e) {
  //    setResult('Error: ' + e.message);
    }
   };

  const saveTest = () => {
    localStorage.setItem('savedTest', JSON.stringify({ description, steps }));
    alert('Test saved locally!');
  };

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">Playwright UI Test Designer</h1>
      <input
        className="border p-2 w-full mb-4"
        placeholder="Test Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <StepList steps={steps} updateStep={updateStep} removeStep={removeStep} addStep={addStep} />
      <TestControls runTest={runTest} saveTest={saveTest} />
      <TestResult result={result} />
    </div>
  );
}
